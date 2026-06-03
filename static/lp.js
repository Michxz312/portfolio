function getInputs() {
    return {
        a1 : parseFloat(document.getElementById("a1").value),
        b1 : parseFloat(document.getElementById("b1").value),
        c1 : parseFloat(document.getElementById("c1").value),
        a2 : parseFloat(document.getElementById("a2").value),
        b2 : parseFloat(document.getElementById("b2").value),
        c2 : parseFloat(document.getElementById("c2").value),
        a3 : parseFloat(document.getElementById("a3").value),
        b3 : parseFloat(document.getElementById("b3").value),
        c3 : parseFloat(document.getElementById("c3").value)
    };
}

function showMatrix(inputs) {
    document.getElementById("matrixDisplay").innerHTML = `
    $$
    \\begin{bmatrix}
    ${inputs.a1} & ${inputs.b1} \\\\
    ${inputs.a2} & ${inputs.b2} \\\\
    ${inputs.a3} & ${inputs.b3}
    \\end{bmatrix}

    \\begin{bmatrix}
    x \\\\
    y
    \\end{bmatrix}
    =

    \\begin{bmatrix}
    ${inputs.c1} \\\\
    ${inputs.c2} \\\\
    ${inputs.c3}
    \\end{bmatrix}

    $$
    `;
    MathJax.typeset();
}

function analyzeSystem(inputs) {
    const { a1, b1, c1, a2, b2, c2, a3, b3, c3 } = inputs;
    showMatrix(inputs);

    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = 
        `solution<br><br>`;
}

function nearlyEqual(a, b, epsilon = 1e-10) {
    return Math.abs(a - b) < epsilon;
}

function drawGraph() {
    let data = [
        createLine(a1,b1,c1,"Line 1"),
        createLine(a2,b2,c2,"Line 2"),
        createLine(a3,b3,c3,"Line 3")
    ];

    Plotly.newPlot('plot', data, {
        title: '2D Geometry of Ax = b',
        xaxis: {title:'x'},
        yaxis: {title:'y'},
        showlegend:true
    });
}

function createLine(a,b,c, name) {
    let x = []
    let y = []
    for (let xi=-10; xi<=10; xi+=0.1) {
        x.push(xi);
        if (Math.abs(b) >= 1e-10) {
            y.push((c- a*xi)/b);
        } else {
            y.push(null);
        }
    }
    return {
        x:x,
        y:y,
        mode:'lines',
        name:name
    }
}
document.getElementById("analyze").addEventListener("click", () => {
    const inputs = getInputs();
    analyzeSystem(inputs);
    drawGraph(inputs);
});