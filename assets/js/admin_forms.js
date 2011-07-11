
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


function tie_many_to_many_event(){

    var url = "/ajax/client/company_directory_many";
    var prefix = "manydirectorycompany_set-";
    var i = 0;

    field = "year"; //test field
    fields = [ 'year', 'directory', 'category' ];
    //directory company many to many
    while ( true ) {
        if ( $("#id_"+prefix+i+"-"+field ).attr("id") === undefined   ){
            break;
        }
        
        for ( var j=0; j < fields.length; j++){
            bind_to = $("#id_"+prefix+i+"-"+fields[j]);
            bind_to.bind("change",function(event){
                
                var name = this.name.split("-")[2] ;
                var num = this.name.split("-")[1] ;
                switch ( name ){
                    case 'year': fill_less( url+"?ask=dir&year="+$(this).val(),  "id_"+prefix+ num +"-directory"   ); break;
                    case 'directory': fill_less( url+"?ask=cat&dir="+$(this).val(),  "id_"+prefix+num +"-category"   ); break;
                    case 'category': fill_less( url+"?ask=subcat&cat="+$(this).val(), "id_"+prefix+num+"-subcategory"  ); break;
                }

            });
            if ( fields[j] != "year") bind_to.empty();

        }


        i= i+1;
    }


}


(function($) {
 $(document).ready(function($) {


    tie_many_to_many_event();


    var main_industry_triger = $("#id_main_industry");

    main_industry_triger.change( function(event){ 
        fill_less( '/ajax/client/industry?main_ind_id='+main_industry_triger.val()+'&ask=choices', "id_specific_industry" );
     });

    var company = getParameterByName("company");
    if( company != "" ){
        $("#id_manycompanyperson_set-0-company").val( company ) ;
    }

    $("#id_country").change( function(event){
        fill_less(  '/ajax/client/country?country='+ $("#id_country").val()+'&ask=choices' , "id_city" );
    });


  
 });
})(django.jQuery);

$ = django.jQuery;

function fill_less( url, field ){
        ///This basically fills a choice field according to a parent one, example fills cities choice field according to given country from a previous choice field
        //url has to be a full ajax url that returns ajax results matching the expected format  {"choices": [[1, "Abha"], [2, "Al Artawiah"],...}
        //If the url doesn't bring any results, it replaces the select field with a text box.


        var selected_val = $( "#" + field ).val()  ;

        var selected = "";
        $( "#" + field ).empty()  ;

        $.get(  url+'&rnd='+Math.floor(Math.random()*11)  , function(data) {

            var choices = data['choices'];

            if ( choices !== undefined ) {
                
                if ( ! $("#"+field).is("select") ) { //was replaced by a text box, now we have choices bring back the select box
                    field_obj = $("#"+field);
                    replace = '<select name="'+field_obj.attr("name")+'"  id="'+field_obj.attr("id")+'"></select>';
                    $("#"+field).after( replace );
                    
                    $("#"+field).remove()
                }

                $("#"+field).append( "<option value='' > ----- </option>"  );         

                for( var i = 0; i < choices.length; i++ ) {

                  if ( choices[i][0] == selected_val ){ selected = "selected"  }else{ selected = ""  } 
                  $("#"+field).append( "<option value="+ choices[i][0] +" "+selected+" >" + choices[i][1] + " </option>"  );         
                  
                }
            }else{
                field_obj = $("#"+field);
                replace = '<input name="'+field_obj.attr("name")+'" class="vTextField" maxlength="255" type="text" id="'+field_obj.attr("id")+'">';
                $("#"+field).after( replace );
                
                $("#"+field).remove();
            }
            
 
        });

}



