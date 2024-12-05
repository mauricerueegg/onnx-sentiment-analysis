function getSentiment(event, text) {
    console.log(text);

    if (!text || event.key !== "Enter") {
        positive.innerHTML = '';
        negative.innerHTML = '';
        return;
    }

    answerPart.style.visibility = "visible";

    // Get Sentiment
    fetch('/sentiment?' + new URLSearchParams({
        text: text,
    }), {
        method: 'GET',
        headers: {}
    }).then(
        response => {
            console.log(response)
            response.json().then(function (text) {
                positive.innerHTML = (parseFloat(text.positive)*100).toFixed(1) + "%";
                negative.innerHTML = (parseFloat(text.negative)*100).toFixed(1) + "%";
            });

        }
    ).then(
        success => console.log(success)
    ).catch(
        error => console.log(error)
    );

}