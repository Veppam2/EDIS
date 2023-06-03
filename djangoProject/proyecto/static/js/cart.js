/**
 * Autor: EDIS
 * Función que se ejecuta cuando el documento está listo
 */
jQuery(document).ready(function ($) {
	// Definición de variables
	var $menu_navigation = $('#main-nav');
	var $cart_trigger = $('#cd-cart-trigger');
	var $lateral_cart = $('#cd-cart');
	var $shadow_layer = $('#cd-shadow-layer');
	
	/**
	 * Abre el carrito
	 */
	$cart_trigger.on('click', function (event) {
		event.preventDefault();
		toggle_panel_visibility($lateral_cart, $shadow_layer, $('body'));
	});
	
  
	/**
	 * Cierra el carrito lateral o el menú lateral
	 */
	$shadow_layer.on('click', function () {
		$shadow_layer.removeClass('is-visible');
		var $current_panel = $lateral_cart.hasClass('speed-in') ? $lateral_cart : $menu_navigation;
		$current_panel.removeClass('speed-in').one('webkitTransitionEnd otransitionend oTransitionEnd msTransitionEnd transitionend', function () {
		  	$('body').removeClass('overflow-hidden');
		});
	});
  
	/**
	 * Regresa al menú principal
	 */
	$('#return-to-menu').on('click', function (event) {
		event.preventDefault();
		$shadow_layer.removeClass('is-visible');
		toggle_panel_visibility($lateral_cart, $shadow_layer, $('body'));
	});
});
  
/**
 * Alterna la visibilidad del panel lateral
 * @param {jQuery} $lateral_panel - El panel lateral a mostrar/ocultar
 * @param {jQuery} $background_layer - La capa de fondo
 * @param {jQuery} $body - El cuerpo del documento
 */
function toggle_panel_visibility($lateral_panel, $background_layer, $body) {
	if ($lateral_panel.hasClass('speed-in')) {
		$lateral_panel.removeClass('speed-in').one('webkitTransitionEnd otransitionend oTransitionEnd msTransitionEnd transitionend', function () {
			$body.removeClass('overflow-hidden');
		});
		$background_layer.removeClass('is-visible');
	} else {
		$lateral_panel.addClass('speed-in').one('webkitTransitionEnd otransitionend oTransitionEnd msTransitionEnd transitionend', function () {
			$body.addClass('overflow-hidden');
		});
		$background_layer.addClass('is-visible');
	}
}
  
/**
 * Mueve la navegación al interior del encabezado en dispositivos de escritorio
 * o después del encabezado en dispositivos móviles
 * @param {jQuery} $navigation - La navegación principal
 * @param {number} $MQ - El punto de quiebre
 */
function move_navigation($navigation, $MQ) {
	if ($(window).width() >= $MQ) {
	  $navigation.detach();
	  $navigation.appendTo('header');
	} else {
	  $navigation.detach();
	  $navigation.insertAfter('header');
	}
}

/**
 * Realiza una solicitud AJAX para modificar el carrito de compras
 * @param {string} url - URL de la solicitud AJAX
 * @param {object} data - Datos a enviar en la solicitud AJAX
 */
function modificarCarrito(url, data) {
	var csrftoken = getCookie('csrftoken');
  
	$.ajax({
	  url: url,
	  type: "POST",
	  data: Object.assign(data, { csrfmiddlewaretoken: csrftoken }),
	  success: function () {
		location.reload();
	  },
	  error: function () {
		alert("Error en la petición AJAX");
	  }
	});
}
  
/**
 * Agrega una cantidad al carrito utilizando AJAX
 * @param {number} alimentoId - ID del alimento
 * @param {number} cantidad - Cantidad a agregar
 */
function agregarCantidad(alimentoId, cantidad) {
	var data = {
	  cartItemId: alimentoId,
	  cantidad: cantidad
	};
	modificarCarrito("/menu-principal/agregar-al-carrito/", data);
}
  
/**
 * Elimina una cantidad del carrito utilizando AJAX
 * @param {number} alimentoId - ID del alimento
 * @param {number} cantidad - Cantidad a eliminar
 */
function eliminarCantidad(alimentoId, cantidad) {
	var data = {
	  alimento_id: alimentoId,
	  cantidad: cantidad
	};
	modificarCarrito("/menu-principal/eliminar-cantidad-carrito/", data);
}
  
/**
 * Elimina todo un alimento del carrito utilizando AJAX
 * @param {number} alimentoId - ID del alimento
 */
function eliminarTotal(alimentoId) {
	var data = {
	  alimento_id: alimentoId
	};
	modificarCarrito("/menu-principal/eliminar-alimento/", data);
}
  
/**
 * Obtiene el valor de una cookie
 * @param {string} name - Nombre de la cookie
 * @returns {string|null} - Valor de la cookie o null si no se encuentra
 */
function getCookie(name) {
	var cookieValue = null;
	if (document.cookie && document.cookie !== '') {
	  var cookies = document.cookie.split(';');
	  for (var i = 0; i < cookies.length; i++) {
		var cookie = cookies[i].trim();
		if (cookie.substring(0, name.length + 1) === (name + '=')) {
		  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
		  break;
		}
	  }
	}
	return cookieValue;
}
  