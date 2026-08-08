const bootScreen = document.getElementById('bootScreen');
const desktop = document.getElementById('desktop');
const bootButton = document.getElementById('bootButton');
const icons = document.querySelectorAll('.app-icon');
const windows = document.querySelectorAll('.window');

bootButton.addEventListener('click', () => {
  bootScreen.hidden = true;
  desktop.hidden = false;
});

icons.forEach(icon => {
  icon.addEventListener('click', () => {
    const target = icon.dataset.window;
    windows.forEach(windowEl => {
      windowEl.classList.toggle('active', windowEl.id === `${target}Window`);
    });
  });
});
