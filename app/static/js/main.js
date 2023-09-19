 
document.addEventListener("DOMContentLoaded", function() {

    // Função para alternar a visibilidade de um elemento
    function toggleVisibility(elementId) {
        var element = document.getElementById(elementId);
        if (element.style.display === "none") {
            element.style.display = "block";
        } else {
            element.style.display = "none";
        }
    }

    // Função para atualizar um gráfico (placeholder, você pode expandir isso com uma biblioteca de gráficos como Chart.js)
    function updateChart(chartId, data) {
        var chart = document.getElementById(chartId);
        // Atualize o gráfico com os novos dados aqui
    }

    // Função para filtrar uma tabela com base em uma consulta de pesquisa
    function filterTable(tableId, query) {
        var table = document.getElementById(tableId);
        var rows = table.getElementsByTagName("tr");
        for (var i = 1; i < rows.length; i++) { // Começa em 1 para pular o cabeçalho da tabela
            var cells = rows[i].getElementsByTagName("td");
            var match = false;
            for (var j = 0; j < cells.length; j++) {
                if (cells[j].innerText.toLowerCase().includes(query.toLowerCase())) {
                    match = true;
                    break;
                }
            }
            rows[i].style.display = match ? "" : "none";
        }
    }

    // Adicione event listeners ou outras inicializações aqui, se necessário

});

