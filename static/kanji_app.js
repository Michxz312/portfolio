async function loadKanji() {
    const res = await fetch('https://kanjiapi.dev/v1/kanji/jlpt-2')
    const vocab = await res.json();
    console.log(vocab)
}

loadKanji();