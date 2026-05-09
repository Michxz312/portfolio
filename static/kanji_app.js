let currentReading = "";
let wordList = [];
let score = 0;

async function getRandomKanjiWords() {
    const res = await fetch('https://kanjiapi.dev/v1/kanji/jlpt-2')
    const vocab = await res.json();
    const kanjiList = await sendKanji(vocab);

    while (true) {
        const randomKanji = kanjiList[Math.floor(Math.random() * kanjiList.length)];
        
        const wordRes = await fetch(`/kanji/jisho/${randomKanji}`);
        const wordData = await wordRes.json();
        const validWords = wordData.data.filter(word => {
            const containsKanji = word.japanese?.some(j => j.word?.includes(randomKanji));
            const isN2 = word.jlpt?.includes("jlpt-n2");
            const noJlpt = !word.jlpt || word.jlpt.length == 0;

            return containsKanji && (isN2 || noJlpt);
        });

        if (validWords.length > 0) {
            return validWords;
        }
    }
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

async function main() {
    const n2Words = await getRandomKanjiWords();
    const index = Math.floor(Math.random() * n2Words.length);
    const kanjiInfo = n2Words[index];

    const word = kanjiInfo.japanese?.[0]?.word;
    console.log(word)
    currentReading = kanjiInfo.japanese?.[0]?.reading;
    wordList.push({"kanji": word, "hiragana": currentReading, "definition":kanjiInfo.senses?.[0]?.english_definitions || []})
    document.getElementById("display").textContent = word;
    summary()
}

function summary() {
    console.log("table:", document.getElementById("word-table"));

    const tbody = document.querySelector("#word-table tbody");

    tbody.innerHTML = wordList.map(item => `
        <tr>
            <td>${item.kanji}</td>
            <td>${item.hiragana}</td>
            <td>${item.definition}</td>
        </tr>
    `).join("");
}

document.getElementById("submit").addEventListener("click", () => {
    const guess = document.getElementById("romaji-input").value.trim();
    if (guess == currentReading) {
        document.getElementById("summary").textContent = "correct!"
    }
    console.log(wordList)
})

document.addEventListener("DOMContentLoaded", () => {
    main();
})

