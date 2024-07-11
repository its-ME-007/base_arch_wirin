const express = require('express');
const axios = require('axios');
const app = express();
const PORT = process.env.PORT || 3000;

const MAPBOX_ACCESS_TOKEN = 'pk.eyJ1Ijoid2lwb2RydmNlIiwiYSI6ImNsdnVzN255YzE5MDYycm55c3hheDhtdTUifQ.lEWdCkssgxZWHlg0eGNkiw';  // Replace with your actual Mapbox access token

app.use(express.static('public'));

app.get('/mapping/directions', async (req, res) => {
    const { origin, destination } = req.query;

    if (!origin || !destination) {
        return res.status(400).send('Origin and destination are required');
    }

    const url = `https://api.mapbox.com/directions/v5/mapbox/driving/${origin};${destination}?access_token=${MAPBOX_ACCESS_TOKEN}&geometries=geojson`;

    try {
        const response = await axios.get(url);
        const route = response.data.routes[0].geometry;
        res.json({ route });
    } catch (error) {
        console.error('Error fetching directions:', error);
        res.status(500).send('Error fetching directions');
    }
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

