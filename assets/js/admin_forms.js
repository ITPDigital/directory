
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
    console.log("doc ready");
    console.log( $("#manydirectorycompany_set-group") ); 
    console.log( $("#id_child-0-parent") );

    var add_row = $("#manydirectorycompany_set-group .add-row a")[0];

    console.log(add_row);

     $("#manydirectorycompany_set-group a").bind("click", function() { 
        console.log( "addd" );  
      } );


  
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


function increment_form_ids(el, to) {
    var from = to-1;
    $(':input', $(el)).each(function(i,e){
          var old_name = $(e).attr('name')
          var old_id = $(e).attr('id')
          $(e).attr('name', old_name.replace(from, to))
          $(e).attr('id', old_id.replace(from, to))
          $(e).val('')
    })
}
 
function add_inline_button() {
    $(".inline-group .add-row a").bind("click", function(e) {
    console.log( "addd" );
        var rows = $(this).parents("div.inline-group").find("tr");
        var last = $(rows[rows.length-1]);
        var copy = last.clone(true);
        if (last.hasClass("row1")) {
            copy.attr("class", "row2");
        } else {
            copy.attr("class", "row1");
        }
        last.after(copy);
        $($(this).parents("div.inline-group").find("input")[0]).val(rows.length);
        increment_form_ids(copy, rows.length-1);
        return false;
    });
}




