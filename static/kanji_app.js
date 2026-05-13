let currentReading = "";
let wordList = [];
let words = []
let currIndex = 0;
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
    clear()
    const index = Math.floor(Math.random() * n2Words.length);
    const kanjiInfo = n2Words[index];

    const currentWord = kanjiInfo.japanese?.[0]?.word;
    words.push(currentWord)
    console.log(currentWord)
    currentReading = kanjiInfo.japanese?.[0]?.reading;
    wordList.push({"kanji": currentWord, "hiragana": currentReading, "definition":kanjiInfo.senses?.[0]?.english_definitions || []})
    document.getElementById("display").textContent = currentWord;
    document.getElementById("submit").classList.add("show");
}

function summary() {
    const tbody = document.querySelector("#word-table");
    tbody.innerHTML = wordList.map(item => `
        <tr>
            <td>${item.kanji}</td>
            <td>${item.hiragana}</td>
            <td>${item.definition.join(", ")}</td>
        </tr>
    `).join("");

    document.getElementById("summary").style.display = "block";
    document.getElementById("submit").classList.remove("hidden")
}

function clear() {
    document.getElementById("correct-answer").textContent = "";
    document.getElementById("display").textContent = "";
    document.getElementById("score").textContent = "";

    document.getElementById("romaji-input").value = "";
}

function resetGame() {
    currentReading = "";
    wordList = [];
    words = []
    currIndex = 0;
    score = 0;
    document.getElementById("summary").style.display = "none";
    document.getElementById("correct-answer").textContent = "";
    document.getElementById("score").textContent = "";

    document.getElementById("romaji-input").value = "";
    
    main();
}

document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("submit").addEventListener("click", () => {
        const guess = document.getElementById("romaji-input").value.trim();
        if (guess == currentReading) {
            document.getElementById("true-false").textContent = "correct!";
            score++;
        }
        else if (guess != currentReading) {
            document.getElementById("true-false").textContent = "false!";
            document.getElementById("correct-answer").textContent = wordList[currIndex].hiragana;
        }
        currIndex += 1;
        document.getElementById("score").textContent = score;

        if (currIndex >= 8) {
            summary()
        } else {
            main()
        }
    });

    main();
})

document.getElementById("reset-btn").addEventListener("click", resetGame);