async function getRandomKanjiWords() {
    const res = await fetch('https://kanjiapi.dev/v1/kanji/jlpt-2')
    const vocab = await res.json();
    const kanjiList = await sendKanji(vocab);

    let n2; 
    while (true) {
        const randomKanji = kanjiList[Math.floor(Math.random() * kanjiList.length)];
        
        const wordRes = await fetch(`/kanji/jisho/${randomKanji}`);
        const wordData = await wordRes.json();
        n2 = wordData.data.filter(kanji => kanji.jlpt && kanji.jlpt[0] === "jlpt-n2")

        if (n2.length > 1) {
            break;
        }
    }
    return n2;
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

const n2Words = getRandomKanjiWords();
console.log(n2Words)
