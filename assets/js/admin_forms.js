
function getParameterByName(name)
{
  name = name.replace(/[\[]/, "\\\[").replace(/[\]]/, "\\\]");
  var regexS = "[\\?&]" + name + "=([^&#]*)";
  var regex = new RegExp(regexS);
  var results = regex.exec(window.location.href);
  if(results == null)
    return "";
  else
    return decodeURIComponent(results[1].replace(/\+/g, " "));
}


(function($) {
 $(document).ready(function($) {

    var main_industry_triger = $("#id_main_industry");

    main_industry_triger.change( function(event){ 
        fill_specific_industry( main_industry_triger.val() , "id_specific_industry" );
     });

    var company = getParameterByName("company");
    if( company != "" ){
        $("#id_manycompanyperson_set-0-company").val( company ) ;
    } 

  
 });
})(django.jQuery);

$ = django.jQuery;

function fill_specific_industry( provider_id, field ){
        var selected_val = $( "#" + field ).val()  ;

        var selected = "";
        $( "#" + field ).empty()  ;

        $.get(  '/ajax/client/industry?main_ind_id='+provider_id+'&ask=choices&rnd='+Math.floor(Math.random()*11)    , function(data) {

            var choices = data['choices'];
            for( var i = 0; i < choices.length; i++ ) {

              if ( choices[i][0] == selected_val ){ selected = "selected"  }else{ selected = ""  } 
              $("#"+field).append( "<option value="+ choices[i][0] +" "+selected+" >" + choices[i][1] + " </option>"  );         
              
            }
   
        });

}



