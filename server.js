const express = require('express');   // Import Express framework for building the server
const cors = require('cors');         // Import CORS middleware to handle Cross-Origin requests
const path = require('path');         // Import path module to work with file and directory paths

const app = express();                // Create an Express application instance
const PORT = process.env.PORT || 3000;  // Set port from environment variable or default to 3000

app.use(cors());  // Enable CORS for all routes to allow requests from other origins

// Serve static files from the 'static' directory under the '/static' URL path
app.use('/static', express.static(path.join(__dirname, 'static')));

// Load courses data from a local JSON file
const courses = require('./data/courses.json');
// Define API endpoint to send courses data as JSON response
app.get('/api/courses', (req, res) => {
  res.json(courses);
});

// Load testimonials data from a local JSON file
const testimonials = require('./data/testimonials.json');
// Define API endpoint to send testimonials data as JSON response
app.get('/api/testimonials', (req, res) => {
  res.json(testimonials);
});

// Start the server and listen on the specified port
app.listen(PORT, () => {
  console.log(`Express server running on port ${PORT}`);
});
