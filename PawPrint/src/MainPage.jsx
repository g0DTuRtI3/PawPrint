import React, { useState, useEffect } from "react";
import MainPageTables from './MainPageTables';
import './MainPage.css';
import MainPageImages from './MainPageImages';
import MainPageButtons from './MainPageButtons';
import EditForm from './EditForm';
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

    const [showForm, setShowForm] = useState(false);
    const [formData, setFormData] = useState({
        petName: '',
        breed: '',
        gender: '',
        id: '',
        status: '',
        age: '',
        weight: '',
        allergies: '',
        vaccination: '',
        checkUpDate: '',
        medication: '',
        ownerName: '',
        phoneNumber: '',
        ownerGender: '',
        email: '',
        address: ''
    });

    const openForm = () => {
        setShowForm(true);
    };

    const closeForm = () => {
        setShowForm(false);
    };

    const handleSave = (data) => {
        setFormData(data);  // Update the form data in MainPage
    };

    return (
        <div className="wrapper">
            <div className="rectangleBorder">
                <MainPageTables formData={formData} />
                <MainPageImages />
                <MainPageButtons onEditClick={openForm} />

                {/* Conditionally render the EditForm */}
                {showForm && <EditForm onClose={closeForm} onSave={handleSave} />}
            </div>
        </div>
    );
}

export default MainPage;
