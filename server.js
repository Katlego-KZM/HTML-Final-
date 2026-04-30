const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.post('/submit-testimonial', (req, res) => {
    const { name, testimonial } = req.body;
    console.log(`Name: ${name}, Testimonial: ${testimonial}`);
    res.status(200).send('Testimonial submitted successfully!');
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});

