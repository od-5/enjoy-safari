/**
 * Created by alexy on 28.05.15.
 */
$(function() {
  $('.popupbutton').fancybox({
    'padding': 37,
    'overlayOpacity': 0.87,
    'overlayColor': '#fff',
    'transitionIn': 'none',
    'transitionOut': 'none',
    'titlePosition': 'inside',
    'centerOnScroll': true,
    'width': 600,
    'minHeight': 310,
    afterClose: function(e){
      $('.ticket-form').trigger('reset');
    }


  });

  $('.popupbutton').on('click', function(e){
    var form = $(this).parent('form');
    var name = form.find('.ticket-form__name').val();
    var phone = form.find('.ticket-form__phone').val();
    $('.pop-form').find('.ticket-form__name__travel').val(name)
    $('.pop-form').find('.ticket-form__phone__travel').val(phone)
  });

  $( ".pop-form" ).validate({
    rules: {
      name: {
        required: true
      },
      phone: {
        required: true
      }
    },
    submitHandler: function(e) {
      $('.pop-form').ajaxSubmit({
          success: function(data){
            $.fancybox.close();
          }
      });
    }
  });

});