/* ================================================================
   QLearn — Quantum particle background + scroll animations
   ================================================================ */

(function () {
    "use strict";

    // ── Quantum Particle Background ──────────────────────────
    const canvas = document.getElementById("quantum-bg");
    if (!canvas) return;
    const ctx = canvas.getContext("2d");

    let W, H;
    const particles = [];
    const PARTICLE_COUNT = 80;
    const CONNECTION_DIST = 150;

    function resize() {
        W = canvas.width = window.innerWidth;
        H = canvas.height = window.innerHeight;
    }
    window.addEventListener("resize", resize);
    resize();

    class Particle {
        constructor() {
            this.x = Math.random() * W;
            this.y = Math.random() * H;
            this.vx = (Math.random() - 0.5) * 0.4;
            this.vy = (Math.random() - 0.5) * 0.4;
            this.r = Math.random() * 2 + 0.5;
            // green or purple tint — mid-tone
            this.color = Math.random() > 0.5
                ? "rgba(92, 224, 194, VAR)"
                : "rgba(180, 142, 237, VAR)";
        }
        update() {
            this.x += this.vx;
            this.y += this.vy;
            if (this.x < 0 || this.x > W) this.vx *= -1;
            if (this.y < 0 || this.y > H) this.vy *= -1;
        }
        draw() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.r, 0, Math.PI * 2);
            ctx.fillStyle = this.color.replace("VAR", "0.45");
            ctx.fill();
        }
    }

    for (let i = 0; i < PARTICLE_COUNT; i++) {
        particles.push(new Particle());
    }

    function drawConnections() {
        for (let i = 0; i < particles.length; i++) {
            for (let j = i + 1; j < particles.length; j++) {
                const dx = particles[i].x - particles[j].x;
                const dy = particles[i].y - particles[j].y;
                const dist = Math.sqrt(dx * dx + dy * dy);
                if (dist < CONNECTION_DIST) {
                    const alpha = (1 - dist / CONNECTION_DIST) * 0.15;
                    ctx.beginPath();
                    ctx.moveTo(particles[i].x, particles[i].y);
                    ctx.lineTo(particles[j].x, particles[j].y);
                    ctx.strokeStyle = `rgba(92, 224, 194, ${alpha})`;
                    ctx.lineWidth = 0.5;
                    ctx.stroke();
                }
            }
        }
    }

    function animate() {
        ctx.clearRect(0, 0, W, H);
        particles.forEach((p) => {
            p.update();
            p.draw();
        });
        drawConnections();
        requestAnimationFrame(animate);
    }
    animate();

    // ── Scroll Reveal for Lessons ────────────────────────────
    const lessons = document.querySelectorAll(".lesson");
    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("visible");
                }
            });
        },
        { threshold: 0.1, rootMargin: "0px 0px -50px 0px" }
    );
    lessons.forEach((el) => observer.observe(el));

    // ── Smooth nav active state ──────────────────────────────
    const navLinks = document.querySelectorAll(".nav-links a");
    const sections = document.querySelectorAll(".module");

    const navObserver = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    const id = entry.target.id;
                    navLinks.forEach((link) => {
                        link.style.color =
                            link.getAttribute("href") === `#${id}`
                                ? "var(--accent-cyan)"
                                : "";
                    });
                }
            });
        },
        { threshold: 0.3 }
    );
    sections.forEach((s) => navObserver.observe(s));

    // ── Code Snippet Tabs ────────────────────────────────────
    document.addEventListener("click", function (e) {
        const btn = e.target.closest(".code-tab-btn");
        if (!btn) return;
        const tabs = btn.closest(".code-tabs");
        if (!tabs) return;
        const target = btn.dataset.tab;

        tabs.querySelectorAll(".code-tab-btn").forEach(function (b) {
            b.classList.toggle("active", b === btn);
        });
        tabs.querySelectorAll(".code-tab-content").forEach(function (c) {
            c.classList.toggle("active", c.dataset.tab === target);
        });
    });
})();
