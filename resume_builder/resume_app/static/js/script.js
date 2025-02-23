window.addEventListener('scroll', function() {
    const scrollPosition = window.scrollY;
    const background = document.querySelector('body.dark-theme');
    background.style.backgroundPositionY = -scrollPosition * 0.5 + 'px';
});