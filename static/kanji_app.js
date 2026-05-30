let currentReading = "";
let wordList = [];
let words = []
let check = false;
let currIndex = 0;
let score = 0;
let isLoading = false;
let stage = 5;

async function getRandomKanjiWords() {
    const res = await fetch(`https://kanjiapi.dev/v1/kanji/jlpt-${stage}`)
    const vocab = await res.json();
    const kanjiList = await sendKanji(vocab);
    console.log(kanjiList)
    while (true) {
        const randomKanji = kanjiList[Math.floor(Math.random() * kanjiList.length)];
        const wordRes = await fetch(`/kanji/jisho/${randomKanji}`);
        const wordData = await wordRes.json();
        const validWords = wordData.data.filter(word => {
            return selectStage(word, randomKanji);
        });
        if (validWords.length > 0 && validWords.length < 5) {
            return validWords[0];
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

function setLoading(load) {
    isLoading = load;

    const btn = document.getElementById("submit");

    btn.disabled = load;
    btn.textContent = load ? "Loading..." : "Submit";
}

function selectStage(word, randomKanji) {
    const containsKanji = word.japanese?.some(j => j.word?.includes(randomKanji));
    if (!containsKanji) return false;

    const jlptLevels = word.jlpt || [];
    const wanikaniTag = word.tags?.find(tag => tag.startsWith("wanikani"));
    const wanikani = wanikaniTag
        ? Number(wanikaniTag.replace("wanikani", ""))
        : 0;

    if (stage == 1) return jlptLevels.includes("jlpt-n1") || wanikani >= 50;
    if (stage == 2) return jlptLevels.includes("jlpt-n2") || (wanikani < 50 && wanikani >= 30);
    if (stage == 3) return jlptLevels.includes("jlpt-n3") || (wanikani < 40 && wanikani >= 20);
    if (stage == 4) return jlptLevels.includes("jlpt-n4") || (wanikani < 25 && wanikani >= 10);
    if (stage == 5) return jlptLevels.includes("jlpt-n5") || (wanikani < 16 && wanikani >= 0);

    return false;
}

async function main() {
    try {
        setLoading(true);   
        const kanjiInfo = await getRandomKanjiWords();
        console.log(kanjiInfo)
        clear()

        const currentWord = kanjiInfo.japanese?.[0]?.word;
        words.push(currentWord)
        currentReading = kanjiInfo.japanese?.[0]?.reading;
        wordList.push({"kanji": currentWord, "hiragana": currentReading, "definition":kanjiInfo.senses?.[0]?.english_definitions || [], "check": check})
        document.getElementById("display").textContent = currentWord;
        document.getElementById("submit").classList.add("show");
    } catch (err) {

    } finally {
        setLoading(false);
    }
}

function summary() {
    document.getElementById("submit").classList.remove("show");
    clear();
    const tbody = document.querySelector("#word-table tbody");
    tbody.innerHTML = wordList.map(item => `
        <tr>
            <td>${item.kanji}</td>
            <td>${item.hiragana}</td>
            <td>${item.definition.join(", ")}</td>
            <td>${item.check=== false?"✗" : "✓"}</td>
        </tr>
    `).join("");

    document.getElementById("summary").style.display = "block";
    document.getElementById("score").textContent = "score: " + score;
}

function clear() {
    document.getElementById("correct-answer").textContent = "";
    document.getElementById("display").textContent = "";
    document.getElementById("true-false").textContent = "";
    document.getElementById("score").textContent = "";

    document.getElementById("romaji-input").value = "";
}

function resetGame() {
    currentReading = "";
    wordList = [];
    words = []
    currIndex = 0;
    score = 0;
    document.getElementById("game-container").style.display = "none";
    document.getElementById("summary").style.display = "none";
    document.getElementById("stages").style.display = "block";

    document.getElementById("true-false").textContent = "";
    document.getElementById("correct-answer").textContent = "";
    document.getElementById("score").textContent = "";
    document.getElementById("romaji-input").value = "";
}

document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".stage-btn").forEach(button => {
        button.addEventListener("click", () => {
            stage = Number(button.dataset.stage);

            document.getElementById("stages").style.display = "none";
            document.getElementById("game-container").style.display = "block";

            main();
        });
    });

    document.getElementById("submit").addEventListener("click", () => {
        const guess = document.getElementById("romaji-input").value.trim();
        if (guess === currentReading) {
            document.getElementById("true-false").textContent = "correct!";
            score++;
            wordList[currIndex].check = true;
        }
        else if (guess != currentReading) {
            document.getElementById("true-false").textContent = "false!";
            document.getElementById("correct-answer").textContent = wordList[currIndex].hiragana;
            wordList[currIndex].check = false;
        }
        currIndex += 1;
        document.getElementById("score").textContent = "score: " + score;

        if (currIndex >= 2) {
            summary()
        } else {
            main()
        }
    });

    document.getElementById("reset-btn").addEventListener("click", resetGame);
    document.getElementById("game-container").style.display = "none";
})

