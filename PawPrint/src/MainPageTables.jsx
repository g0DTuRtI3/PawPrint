import './MainPage.css';

function MainPageTables({ formData }) {
    return (
        <div className="tables-container">
            <div className="generalTable">
                <div className="table-row">
                    <span className="label">{formData.petName}</span>
                    <div className="table-cell"></div>
                </div>
                <div className="table-row">
                    <span className="label" id="breedValue">{formData.breed}</span>
                    <div className="table-cell"></div>
                </div>
                <div className="table-row">
                    <span className="label" id="genderValue">{formData.gender}</span>
                    <div className="table-cell"></div>
                </div>
                <div className="table-row">
                    <span className="label" id="id_Value">{formData.id}</span>
                    <div className="table-cell"></div>
                </div>
                <div className="table-row">
                    <span className="label" id="statusValue">{formData.status}</span>
                    <div className="table-cell"></div>
                </div>
            </div>
            <div className="advancedTable">
                <span id="medicalLabel">Medical</span>
                <span id="ownerLabel">Owner</span>
                <div className='medicalTable'>
                    <div className="table-row2">
                        <span className="label2">Age:</span>
                        <span className="label2" id="ageValue">{formData.age}</span>
                        <div className="table-cell2"></div>
                    </div>
                    <div className="table-row2">
                        <span className="label2">Weight:</span>
                        <span className="label2" id="weightValue">{formData.weigth}</span>
                        <div className="table-cell2"></div>
                    </div>
                    <div className="table-row2">
                        <span className="label2">Allergies:</span>
                        <span className="label2" id="allergiesValue">{formData.allergies}</span>
                        <div className="table-cell2"></div>
                    </div>
                    <div className="table-row2">
                        <span className="label2">Vaccination:</span>
                        <span className="label2" id="vaccinationValue">{formData.vaccination}</span>
                        <div className="table-cell2"></div>
                    </div>
                    <div className="table-row2">
                        <span className="label2">Check Up Date:</span>
                        <span className="label2" id="checkUpDateValue">{formData.checkUpDate}</span>
                        <div className="table-cell2"></div>
                    </div>
                    <div className="table-row2">
                        <span className="label2">Medication:</span>
                        <span className="label2" id="medicationValue">{formData.medication}</span>
                        <div className="table-cell2"></div>
                    </div>
                </div>
                <div className='ownerTable'>
                    <div className="table-row2">
                        <span className="label2">Name:</span>
                        <span className="label2" id="nameValue">{formData.ownerName}</span>
                        <div className="table-cell2"></div>
                    </div>
                    <div className="table-row2">
                        <span className="label2">Phone Number:</span>
                        <span className="label2" id="phoneNumberValue">{formData.phoneNumber}</span>
                        <div className="table-cell2"></div>
                    </div>
                    <div className="table-row2">
                        <span className="label2">Gender:</span>
                        <span className="label2" id="ownerGenderValue">{formData.ownerGender}</span>
                        <div className="table-cell2"></div>
                    </div>
                    <div className="table-row2">
                        <span className="label2">Email:</span>
                        <span className="label2" id="emailValue">{formData.email}</span>
                        <div className="table-cell2"></div>
                    </div>
                    <div className="table-row2">
                        <span className="label2">Address:</span>
                        <span className="label2" id="addressValue">{formData.address}</span>
                        <div className="table-cell2"></div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default MainPageTables;
