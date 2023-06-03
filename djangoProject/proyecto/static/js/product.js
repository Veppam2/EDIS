/**
 * Autor: EDIS
 * Función para incrementar la cantidad del input
 */
function increment() {
    var input = document.getElementById("input1");
    input.value = parseInt(input.value) + 1;
    updateCartItemTotal();
  }
  
  /**
   * Función para decrementar la cantidad del input
   */
  function decrement() {
    var input = document.getElementById("input1");
    var value = parseInt(input.value);
    if (value > 1) {
      input.value = value - 1;
      updateCartItemTotal();
    }
  }
  
  /**
   * Función para actualizar el precio total del carrito
   */
  function updateCartItemTotal() {
    var input = document.getElementById("input1");
    var qty = parseInt(input.value);
    var price = parseFloat(document.getElementById("cartItemPrice").innerText.replace("$", ""));
    var total = qty * price;
    document.getElementById("cartItemTotal").innerText = "$" + total.toFixed(2);
    document.getElementById("cantidad").value = qty;
  }
  
  /** 
   * Función que se ejecuta cuando el documento HTML está listo
   */ 
  $(document).ready(function () {
    // Evento click en el botón del carrito
    $('.cartButton').click(function () {
        // Obtener los datos del alimento seleccionado
        var alimento = $(this).data();
        
        // Actualizar los elementos del modal con los datos del alimento seleccionado
        $('#cartItemId').val(alimento.id);
        $('#cartItemImage').attr('src', alimento.imagen);
        $('#cartItemName').text(alimento.nombre);
        $('#cartItemPrice').text('$' + alimento.precio);
        $('#cantidad').val('1');
    
        // Calcular y actualizar el precio total al cambiar la cantidad
        $('#input1').on('input', function () {
            var qty = $(this).val();
            var total = alimento.precio * qty;
            $('#cartItemTotal').text('$' + total);
            $('#cantidad').val(qty);
        });

        // Inicializar el valor total
        var qty = $('#input1').val();
        var total = alimento.precio * qty;
        $('#cartItemTotal').text('$' + total);

        // Mostrar el modal del carrito
        $('#cartModal').modal('show');
    });
    
    // Desactivar el modal al hacer clic en el botón "Cerrar"
    $('#cartModal').on('hidden.bs.modal', function () {
        $(this).find('input').val('1'); // Restaurar el valor predeterminado de la cantidad
    });
});
  