import React, { useState } from 'react';
import './MainPage.css';

function EditForm({ onClose, onSave }) {
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

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setFormData(prevData => ({
            ...prevData,
            [name]: value,
        }));
    };

    const handleSave = (e) => {
        e.preventDefault(); // Prevent form submission
        onSave(formData);  // Pass the form data back to the parent component (MainPage)
        onClose();  // Close the form
    };

    return (
        <div className="edit-form-container">
            <form onSubmit={handleSave}> {/* Use onSubmit for handling Save action */}
                <div className="form-row">
                    <label>Pet Name:</label>
                    <input
                        type="text"
                        name="petName"
                        value={formData.petName}
                        onChange={handleInputChange}
                    />
                </div>
                <div className="form-row">
                    <label>Breed:</label>
                    <input
                        type="text"
                        name="breed"
                        value={formData.breed}
                        onChange={handleInputChange}
                    />
                </div>
                <div className="form-row">
                    <label>Gender:</label>
                    <input
                        type="text"
                        name="gender"
                        value={formData.gender}
                        onChange={handleInputChange}
                    />
                </div>
                <div className="form-row">
                    <label>ID:</label>
                    <input
                        type="text"
                        name="id"
                        value={formData.id}
                        onChange={handleInputChange}
                    />
                </div>
                <div className="form-row">
                    <label>Status:</label>
                    <input
                        type="text"
                        name="status"
                        value={formData.status}
                        onChange={handleInputChange}
                    />
                </div>
                <div className="form-row">
                    <label>Age:</label>
                    <input
                        type="text"
                        name="age"
                        value={formData.age}
                        onChange={handleInputChange}
                    />
                </div>
                <div className="form-row">
                    <label>Weight:</label>
                    <input
                        type="text"
                        name="weight"
                        value={formData.weight}
                        onChange={handleInputChange}
                    />
                </div>
                <div className="form-row">
                    <label>Allergies:</label>
                    <input
                        type="text"
                        name="allergies"
                        value={formData.allergies}
                        onChange={handleInputChange}
                    />
                </div>
                <div className="form-row">
                    <label>Vaccination:</label>
                    <input
                        type="text"
                        name="vaccination"
                        value={formData.vaccination}
                        onChange={handleInputChange}
                    />
                </div>
                <div className="form-row">
                    <label>Check Up Date:</label>
                    <input
                        type="text"
                        name="checkUpDate"
                        value={formData.checkUpDate}
                        onChange={handleInputChange}
                    />
                </div>
                <div className="form-row">
                    <label>Medication:</label>
                    <input
                        type="text"
                        name="medication"
                        value={formData.medication}
                        onChange={handleInputChange}
                    />
                </div>
                <div className="form-row">
                    <label>Owner Name:</label>
                    <input
                        type="text"
                        name="ownerName"
                        value={formData.ownerName}
                        onChange={handleInputChange}
                    />
                </div>
                <div className="form-row">
                    <label>Phone Number:</label>
                    <input
                        type="text"
                        name="phoneNumber"
                        value={formData.phoneNumber}
                        onChange={handleInputChange}
                    />
                </div>
                <div className="form-row">
                    <label>Owner Gender:</label>
                    <input
                        type="text"
                        name="ownerGender"
                        value={formData.ownerGender}
                        onChange={handleInputChange}
                    />
                </div>
                <div className="form-row">
                    <label>Email:</label>
                    <input
                        type="text"
                        name="email"
                        value={formData.email}
                        onChange={handleInputChange}
                    />
                </div>
                <div className="form-row">
                    <label>Address:</label>
                    <input
                        type="text"
                        name="address"
                        value={formData.address}
                        onChange={handleInputChange}
                    />
                </div>

                {/* Save and Back buttons */}
                <div className="form-actions">
                    <button type="submit">Save</button>
                    <button type="button" onClick={onClose}>Back</button>
                </div>
            </form>
        </div>
    );
}

export default EditForm;
