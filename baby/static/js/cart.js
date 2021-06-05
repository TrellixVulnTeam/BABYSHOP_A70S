var updateBtns = document.getElementsByClassName('update-cart')

for (var j=0;j<updateBtns.length;j++)
{
    updateBtns[j].addEventListener('click',function() { 
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('USER:',user)
        console.log(productId)

        if(user === 'AnonymousUser')
        {
             console.log("Not logged in");
        }
        else
        {
            updateUserOrder(productId,action)
        }
    })
}

function updateUserOrder(productId, action){
	console.log('User is authenticated, sending data...')

		var url = '/update_item/'

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
                'X-CSRFToken':csrftoken,
 			}, 
			body:JSON.stringify({'productId':productId, 'action':action})
		})
		.then((response) => {
		   return response.json(); 
		})
		.then((data) => {
		     console.log('data:',data)
             location.reload()
		});
}
