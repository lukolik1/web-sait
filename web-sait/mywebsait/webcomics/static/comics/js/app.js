var click = 0;



function chekend() {
	let chek = document.getElementById("range-input").checked


	if (chek == true) {
		document.body.style.background = "Black";




		document.getElementById("people-white").style.display = 'none';
		document.getElementById("people-black").style.display = 'block';


		document.getElementById("fonk-img-lun").style.display = 'block';
		document.getElementById("fonk-img-sun").style.display = 'none';

		document.querySelectorAll('span').forEach(e => e.className = 'white');
		document.querySelectorAll('p').forEach(e => e.className = 'white');
		document.querySelectorAll('li').forEach(e => e.className = 'white');
		document.querySelectorAll('h1').forEach(e => e.className = 'white');
		
		for(var i = 0; i < 100; i++){
			 document.getElementById('text-a').style.color = "white";
		}

		

	} else {
		document.body.style.background = "white";


		document.getElementById("people-white").style.display = 'block';
		document.getElementById("people-black").style.display = 'none';



		document.getElementById("fonk-img-sun").style.display = 'block';
		document.getElementById("fonk-img-lun").style.display = 'none';


		document.querySelectorAll('span').forEach(e => e.className = 'black');
		document.querySelectorAll('p').forEach(e => e.className = 'black');
		document.querySelectorAll('li').forEach(e => e.className = 'black');
		document.querySelectorAll('h1').forEach(e => e.className = 'black');

		for(var i = 0; i < 100; i++){
			 document.getElementById('text-a').style.color = "black";
		}
		

		

	}


}







function MenuClick() {
 		
 	const card = document.querySelector('.content-link');

 	if(click){
 	 
 			
	 card.style.display = 'none';
	 click = 0;
	 
	 
	
 	} else {
 		card.style.display = 'flex';
 		click = 1;
 	} 


}


function counter_fn() {
      var counter = document.getElementById("cntr");
      var count = 0;
      count = parseInt(counter.innerHTML);
      count = count + 1;
      counter.innerHTML = count;
    }
    window.onload = counter_fn;
