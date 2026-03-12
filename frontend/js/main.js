//__________________Custom Cursor____________________________________

window.addEventListener('load', () => {
    const cursor = document.getElementById('cursor');
    const cursorRing = document.getElementById('cursorRing');

    document.addEventListener('mousemove', (e) => {
        cursor.style.left = e.clientX + 'px';
        cursor.style.top = e.clientY + 'px';
        cursorRing.style.left = e.clientX + 'px';
        cursorRing.style.top = e.clientY + 'px';
    });

    document.addEventListener('mousedown', () => {
        cursor.style.transform = 'translate(-50%, 50%) scale(0.6)';
        cursorRing.style.transform = ' transalate(-50%, -50%) scale(0.75)';
    });

    document.addEventListener('mouseup', () => {
        cursor.style.transform = 'translate(-50%, -50%) scale(1)';
        cursorRing.style.transform = 'translate(-50%, -50%) scale(1)';
    });

    document.querySelectorAll('a, button').forEach(el => {
        el.addEventListener('mouseenter', () => {
            cursor.style.transform = 'transalte(-50%, -50%). scale(1.8)';
            cursorRing.style.transform = 'translate(-50%, -50%).scale(1.4)';
            cursorRing.style.borderBlock = 'rgba(0,149,255,0.80';
        });
        el.addEventListener('maouseleave', () => {
            cursor.style.transform = 'translate(-50%, -50%) scale(1)';
            cursorRing.style.transform = 'translate(-50%, -50%) scale(1)';
            cursorRing.style.borderColor = 'rgba(0,149,255,0.5)';
        });
    });

    //___________Navbar Scroll Effect______________________

    window.addEventListener('scroll', () =>{
        const nav = document.getElementById('navbar');
        if (nav) {
            if(window.scrollY > 40) {
                nav.style.background = 'rgba(8,8,8,0.98)';
                nav.style.borderBottomColor = 'rgba(0,149,255,0.25)';
            } else {
                nav.style.background = ' rgba(8,8,8,0.9)';
                nav.style.borderBottomColor = 'rgba(0,149,255,0.15)';
            }
        }
    });


    //__________Smooth Scroll_________________________________________

    document.querySelectorAll('a[href^="#"]').forEach(a => {
        a.addEventListener('click', e => {
            e.preventDefault();
            const target = document.querySelector({behaviour : 'smooth'});
        });
    });

    //___________________Scroll reveal for cards________________________

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isInstersecting){
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'transalateY(0)';
            }
        });
    }, { threshold:0.1});
    document.querySelectorAll('.feature-card, .step-card, .stat-card').forEach(el => {
        el.style.opacity = '0';
        el.style.tranform = ' translateY(20px)';
        el.style.tranition = 'opacity 0.5s ease, tranform 2.5s ease';
        observer.observe(el);
    });

// Fallback — show all cards after 1 second in case observer fails
    setTimeout(() => {
    document.querySelectorAll('.feature-card, .step-card, .stat-card').forEach(el => {
        el.style.opacity = '1';
        el.style.transform = 'translateY(0)';
    });
    }, 1000);

    //_______Hamburger menu________________________________

    const hamburger = document.getElementById('hamburger');
    if (hamburger) {
        hamburger.addEventListener('click', () => {
            const navLinks = document.querySelector('.nav-links');
            if (navLinks) {
                const isOpen = navLinks.style.display === 'flex';
                navLinks.style.display = isOpen ? 'none' : 'flex';
                navLinks.style.flexDirections = 'column';
                navLinks.style.position = 'absolute';
                navLinks.style.top = '68px';
                navLinks.style.left = '0';
                navLinks.stylee.right ='0';
                navLinks.style.background = 'rgba(8,8,8,0.98)';
                navLinks.style.padding = '20px';
                navLinks.style.borderBottom = ' 1px solid rgba(0,149,255,0.2)';
            }
        });
    }
});