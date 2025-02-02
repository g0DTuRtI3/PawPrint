import MainPageTables from './MainPageTables';
import './MainPage.css';
import MainPageImages from './MainPageImages';
import MainPageButtons from './MainPageButtons';

import React, { useState, useEffect } from 'react'
import axios from 'axios'

function MainPage() {
    // State to store data fetched from the API
    const [animalData, setAnimalData] = useState(null);

    // Fetch data when the component mounts
    useEffect(() => {
        // Fetching data from your Flask API
        // You can replace '/api/database/<database_name>/ID/<ID>' with the actual URL
        axios.post('http://127.0.0.1:5000/api/database/<database_name>/obj/<data>/', animalData)  // Adjust URL
            .then(response => {
                console.log('Data saved:', response.data);
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }, []); // Empty dependency array means this effect runs once when the component mounts


    return (
        <div className="wrapper">
            <div className="rectangleBorder">
                <MainPageTables></MainPageTables>
                <MainPageImages></MainPageImages>
                <MainPageButtons></MainPageButtons>
            </div>
        </div>
    );
}

export default MainPage;
