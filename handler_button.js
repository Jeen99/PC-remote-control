function test(id) 
{	
	if (id.getAttribute("id") == "shutdown")
		if (!confirm("Вы уверены?"))
			return;
	var request = new XMLHttpRequest();
	var params = 'par=' + id.getAttribute("id");
	url = 'cgi-bin/control.py?' + params;
	request.open('GET',url,true);
	/* request.addEventListener('readystatechange', function() {
		if ((request.readyState==4) && (request.status==200)) {
		  alert(request.responseText);
		}
	}); */
	request.send(); // Отправка запроса на сервер
};

function touch(ID)
{
	var input_ = document.getElementById(input);
	input_.value = event.pageX + ':' + event.pageY;	
}

function funct() 
{
	var obj = document.getElementById('touch');
	var input_ = document.getElementById('input');
	obj.addEventListener('touchmove', function(event) {
	  // If there's exactly one finger inside this element
	  if (event.targetTouches.length == 1) {
		var touch = event.targetTouches[0];
		// Place element where the finger is
		input_.value = touch.pageX + 'px';
		input_.value += touch.pageY + 'px';
	  }
	}, false);
}