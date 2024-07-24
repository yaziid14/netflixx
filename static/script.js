var video = document.getElementById('background-video');
// Pause the video after it has played once
video.addEventListener('ended', function () {
    this.pause();
    document.getElementById('video-container').style.display = 'none';
    document.querySelector('.pics').classList.add('bod')
});
// Play the video
video.play();

function masuk() {
    let email = $('#inputemail').val();
    let password = $('#inputpw').val();

    // console.log(email, password)

    $.ajax({
        type: "POST",
        url: "/akun",
        data: {
            email_give: email,
            password_give: password
        },
        success: function(response) {
            alert("Incorrect Password")
            window.location.replace("/")
        }
    });
}