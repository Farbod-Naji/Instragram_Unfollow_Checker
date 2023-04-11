async function OutputLog(title,inputText) {
    
    const chat = document.createElement("p");

    const chatLog = document.getElementById("chat");
    console.log(chatLog);
    title = "[" + title + "]: "
    chat.innerHTML =  title.bold() + inputText;
    chatLog.append(chat);    
}

OutputLog("Link-State", "from A to C")
OutputLog("Distance-Vector", "from A to B")

