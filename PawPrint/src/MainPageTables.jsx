import './MainPage.css';

function MainPageTables() {
    return (
        <div className="tables-container">
            <div className="generalTable">
                <div className="table-row">
                    <span className="label">Name</span>
                    <div className="table-cell"></div>
                </div>
                <div className="table-row">
                    <span className="label">Breed</span>
                    <div className="table-cell"></div>
                </div>
                <div className="table-row">
                    <span className="label">Gender</span>
                    <div className="table-cell"></div>
                </div>
                <div className="table-row">
                    <span className="label">ID</span>
                    <div className="table-cell"></div>
                </div>
                <div className="table-row">
                    <span className="label">Status</span>
                    <div className="table-cell"></div>
                </div>
            </div>
            <div className="advancedTable">
                <span id="medicalLabel">Medical</span>
                <span id="ownerLabel">Owner</span>
                <div className='medicalTable'>
                    <div className="table-row2">
                        <span className="label2">Age:</span>
                        <span className="label2" id="ageValue"></span>
                        <div className="table-cell2"></div>
                    </div>
                    <div className="table-row2">
                        <span className="label2">Weight:</span>
                        <span className="label2" id="weightValue"></span>
                        <div className="table-cell2"></div>
                    </div>
                    <div className="table-row2">
                        <span className="label2">Allergies:</span>
                        <span className="label2" id="allergiesValue"></span>
                        <div className="table-cell2"></div>
                    </div>
                    <div className="table-row2">
                        <span className="label2">Vaccination:</span>
                        <span className="label2" id="vaccinationValue"></span>
                        <div className="table-cell2"></div>
                    </div>
                    <div className="table-row2">
                        <span className="label2">Check Up Date:</span>
                        <span className="label2" id="checkUpDateValue"></span>
                        <div className="table-cell2"></div>
                    </div>
                    <div className="table-row2">
                        <span className="label2">Medication:</span>
                        <span className="label2" id="medicationValue"></span>
                        <div className="table-cell2"></div>
                    </div>
                </div>
                <div className='ownerTable'>
                    <div className="table-row2">
                        <span className="label2">Name:</span>
                        <span className="label2" id="nameValue"></span>
                        <div className="table-cell2"></div>
                    </div>
                    <div className="table-row2">
                        <span className="label2">Phone Number:</span>
                        <span className="label2" id="phoneNumberValue"></span>
                        <div className="table-cell2"></div>
                    </div>
                    <div className="table-row2">
                        <span className="label2">Pronouns:</span>
                        <span className="label2" id="pronounsValue"></span>
                        <div className="table-cell2"></div>
                    </div>
                    <div className="table-row2">
                        <span className="label2">Email:</span>
                        <span className="label2" id="emailValue"></span>
                        <div className="table-cell2"></div>
                    </div>
                    <div className="table-row2">
                        <span className="label2">Address:</span>
                        <span className="label2" id="addressValue"></span>
                        <div className="table-cell2"></div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default MainPageTables;
