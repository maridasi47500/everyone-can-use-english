$(function(){
$(".insereralphabet").click(function() {
	var mylink=$(this)[0];
  var textarea=document.getElementById("champ_mot_alphabet");
    var start = textarea.selectionStart;

    // Obtain the index of the last selected character
    var finish = textarea.selectionEnd;

    // Obtain the selected text
    var sel = textarea.value.substring(start, finish);
  let first = textarea.value.slice(0, textarea.selectionStart);
  let rest = textarea.value.slice(textarea.selectionEnd, textarea.value.length);

  textarea.value = first +mylink.innerHTML + rest;

  // Bonus: place cursor behind replacement
	textarea.focus();
  textarea.selectionStart = (first+mylink.innerHTML).length;
  textarea.selectionEnd = (first+mylink.innerHTML).length;

});

});
