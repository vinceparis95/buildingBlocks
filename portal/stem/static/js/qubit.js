
////////////////////////////

// qubit with h gate

var state = anime.timeline({
    loop:true,
    duration: 27
});


function entangle() {
    state
        .add({
            targets: '.container54',
            keyframes: [
                {translateX: -19}

            ],
            background: 'rgb(255,0,199)',
            direction: 'alternate',
            easing: 'linear',
            autoplay: false
        })
                .add({
            targets: '.container54',
            keyframes: [
                {translateX: 19},
            ],
            background: 'rgb(13,255,2)',
            direction: 'alternate',
            easing: 'linear',
            autoplay: false
        });



    return (
        <div>Allah'u'Abha
        </div>
    );

}





/////////////////////////////////