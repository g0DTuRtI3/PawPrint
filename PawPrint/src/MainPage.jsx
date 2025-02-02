import React, { useState } from "react";
import MainPageTables from './MainPageTables';
import './MainPage.css';
import MainPageImages from './MainPageImages';
import MainPageButtons from './MainPageButtons';
import EditForm from './EditForm';

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
