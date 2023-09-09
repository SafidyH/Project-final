function connectWebSocket() {
    const socket = new WebSocket("ws://localhost:8000/ws/some_path/");  // Remplacez l'URL par la vôtre

    socket.onopen = () => {
        console.log("Connexion WebSocket établie");
        // Vous pouvez ajouter des actions supplémentaires ici
    };

    socket.onmessage = (event) => {
        const message = JSON.parse(event.data);
        console.log("Message reçu du serveur WebSocket:", message);
        // Traitez le message reçu du serveur
    };

    socket.onclose = () => {
        console.log("Connexion WebSocket fermée");
        // Vous pouvez ajouter des actions supplémentaires ici
    };

    socket.onerror = (error) => {
        console.error("Erreur WebSocket:", error);
    };
}

window.addEventListener("load", connectWebSocket);

function sendMessage(messageText) {
    const message = {
        type: "chat.message",
        text: messageText,
    };
    socket.send(JSON.stringify(message));
}
