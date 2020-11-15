function refresh_all_cards() {
    $.ajax({
        method: "GET",
        url: "/api/all",
        dataType: "json",
        statusCode: {
            200: function (data){
                var i;
                for (i = 0; i < data.length; i++) {
                    update_card_info(data[i])
                }
            }
        }
    })
}

function refresh_single_card(name) {
    $.ajax({
        method: "GET",
        url: "/api/single/"+name,
        dataType: "json",
        statusCode: {
            200: function (data) {
                update_card_info(data)
            }
        },
    })
}

function update_card_info(data) {
    document.getElementById(data.personId+"-calls").innerText = data.calls;
    document.getElementById(data.personId+"-emails").innerText = data.emails;
    document.getElementById(data.personId+"-chats").innerText = data.chats;
    document.getElementById(data.personId+"-chatAFR").innerText = data.chatAFR;
    document.getElementById(data.personId+"-emailAFR").innerText = data.emailAFR;
    document.getElementById(data.personId+"-phoneQueue").innerText = data.phoneStatus;
    document.getElementById(data.personId+"-chatQueue").innerText = data.chatStatus;



}


setInterval(refresh_all_cards, 5000)