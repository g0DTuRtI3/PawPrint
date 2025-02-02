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
        const databaseName = "my_database";
        const url = `http://127.0.0.1:5000/api/database/${databaseName}/`;
        
        // Fetching data from your Flask API
        axios.post(url, animalData)
            .then(response => {
                console.log('Data saved:', response.data);
                setResponseData(response.data);
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }, [animalData]);


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
