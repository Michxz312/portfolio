async function loadKanji() {
    const res = await fetch('https://kanjiapi.dev/v1/kanji/jlpt-2')
    const vocab = await res.json();
    sendKanji(vocab)
}

async function sendKanji(data) {
    const res = await fetch("/kanji/api", {
        method:"POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });

    const result = await res.json();
    console.log(data)
}

loadKanji();