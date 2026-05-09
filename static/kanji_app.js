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

    localStorage.setItem("reading", JSON.stringify(kanjiInfo.japanese[0].reading))
    localStorage.setItem("word", JSON.stringify(kanjiInfo.japanese[0].word))
    localStorage.setItem("definition", JSON.stringify(kanjiInfo.senses[0].english_definitions))
}

main();