document.addEventListener('DOMContentLoaded', function() {
    const summaryTextarea = document.getElementById('summary-textarea');
    const articlesList = document.getElementById('articles-list');

    // Make API request to fetch summary from the text file
    fetch('summary.txt')
        .then(response => response.text())
        .then(summary => {
            summaryTextarea.value = summary;
        })
        .catch(error => {
            console.error('Error fetching summary:', error);
        });

    // Make API request to fetch recent financial news articles
    const newsApiKey = '6165a742479343b3951dd1960ea19634';
    const sources = ['Forbes', 'WSJ', 'Bloomberg']; // Specify your desired news sources

    fetch(`https://newsapi.org/v2/top-headlines?apiKey=${newsApiKey}&sources=${sources.join(',')}&pageSize=10`)
        .then(response => response.json())
        .then(data => {
            if (data.status === 'ok') {
                const articles = data.articles;
                articles.forEach(article => {
                    const li = document.createElement('li');
                    li.innerHTML = `
                        <h3>${article.title}</h3>
                        <p>${article.description}</p>
                        <a href="${article.url}" target="_blank">Read More</a>
                    `;
                    articlesList.appendChild(li);
                });
            } else {
                console.error('Error fetching news articles:', data.message);
            }
        })
        .catch(error => {
            console.error('Error fetching news articles:', error);
        });
});
