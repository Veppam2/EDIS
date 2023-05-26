"use strict";

document.addEventListener("DOMContentLoaded", () => {
    Array.from(document.querySelectorAll('[data-background]')).forEach(el => {
      el.style.background = `url(${el.getAttribute('data-background')})`;
    });
  });