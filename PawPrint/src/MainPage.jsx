import React, { useState } from "react";
import MainPageTables from './MainPageTables';
import './MainPage.css';
import MainPageImages from './MainPageImages';
import MainPageButtons from './MainPageButtons';
import EditForm from './EditForm';
import axios from 'axios';

function MainPage() {
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
        // Update the form data in MainPage
        setFormData(data);

        // Send POST request after form data is updated
        const databaseName = "my_database";
        const url = `http://127.0.0.1:8080/api/database/${databaseName}/`;

        // Make POST request to save the data
        axios.post(url, data)
            .then(response => {
                console.log('Data saved:', response.data);
            })
            .catch(error => {
                console.error('Error:', error);
            });

        // Close the form after saving data
        setShowForm(false);
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
