"use strict";

/**
 * Autor: EDIS
 * Establece el fondo de los elementos con el atributo "data-background"
 */
document.addEventListener("DOMContentLoaded", () => {
  Array.from(document.querySelectorAll('[data-background]')).forEach(el => {
    el.style.background = `url(${el.getAttribute('data-background')})`;
  });
});