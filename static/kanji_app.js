async function loadKanji() {
    const res = await fetch('https://kanjiapi.dev/v1/kanji/jlpt-2')
    const vocab = await res.json();
    const result = await sendKanji(vocab);
    return result;
}

async function sendKanji(data) {
    const res = await fetch("/kanji/api", {
        method:"POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });

    const result = await res.json();
    localStorage.setItem("result", JSON.stringify(result));
    return result;
}

async function getRandomWords(kanji) {
    const res = await fetch(`/kanji/jisho/${kanji}`);
    const data = await res.json();
    console.log(data)
    return data.data.filter(item =>
        item.japanese.some(j => j.word && j.word.includes(kanji))
    );
    
}

async function quizKanji() {
    const kanjiList = JSON.parse(localStorage.getItem("result"));
    const randomIndex = Math.floor(Math.random() * kanjiList.length);
    const kanji = await getRandomWords(kanjiList[randomIndex]);
    console.log(kanji)
    
}

loadKanji();

quizKanji();