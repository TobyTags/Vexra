import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js";
import { getAuth, signInWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-auth.js";
import { getFirestore, collection, getDocs, addDoc, query, where } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js";

document.addEventListener('DOMContentLoaded', async function() {
    try {
        const response = await fetch('/firebase-config');
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        const firebaseConfig = await response.json();

        // Initialize Firebase
        const app = initializeApp(firebaseConfig);
        const auth = getAuth(app);
        const db = getFirestore(app);

        // This is for the sign up form
        const signupForm = document.getElementById('signin-form');
        if (signupForm) {
            signupForm.addEventListener('submit', async function(event) {
                event.preventDefault(); // Prevent form submission

                const rawUsername = document.getElementById('usernamelog').value.trim();
                const rawEmail = document.getElementById('emaillog').value.trim();
                const rawPassword = document.getElementById('passwordlog').value.trim();
                const reEnterEmail = document.getElementById('re-enter-email').value.trim();
                const reEnterPassword = document.getElementById('re-enter-password').value.trim();
                
                if (rawEmail === reEnterEmail) {
                    if (rawPassword === reEnterPassword) {
                        if (rawUsername && rawPassword) { // Check if fields are not empty
                            try {
                                // Encrypt the data
                                const encryptedPassword = await encryptData(rawPassword);
                                const encryptedEmail = await encryptData(rawEmail);
                                const encryptedUsername = await encryptData(rawUsername);

                                // Check if the username already exists
                                const usernameQuery = query(collection(db, "WMLogin"), where("username", "==", encryptedUsername));
                                const usernameSnapshot = await getDocs(usernameQuery);

                                // Check if the email already exists
                                const emailQuery = query(collection(db, "WMLogin"), where("email", "==", encryptedEmail));
                                const emailSnapshot = await getDocs(emailQuery);

                                if (!usernameSnapshot.empty) {
                                    alert('Username already exists. Please pick a different name.');
                                } else if (!emailSnapshot.empty) {
                                    alert('Email already exists. Please use a different email.');
                                } else {
                                    // If username does not exist, add the new user
                                    const docRef = await addDoc(collection(db, "WMLogin"), {
                                        username: encryptedUsername,
                                        email: encryptedEmail,
                                        password: encryptedPassword
                                    });
                                    console.log("Document written with ID: ", docRef.id);

                                    // Save the username to local storage
                                    localStorage.setItem('WMcreds', encryptedUsername);
                                    localStorage.setItem('isAuthenticated', 'true');

                                    // Print out the variables using alert
                                    //alert('Username: ' + encryptedUsername + '\nEmail: ' + encryptedEmail + '\nPassword: ' + encryptedPassword);

                                    alert('Sign up successful!');
                                    window.location.href = '/logedin'; // redirect back to main page
                                }
                            } catch (e) {
                                console.error("Error checking username or adding document: ", e);
                                alert('Error signing up!');
                            }
                        } else {
                            alert('Please fill in both username and password fields.');
                        }
                    } else {
                        alert("Passwords do not match");
                    }
                } else {
                    alert("Emails do not match");
                }
            });
        }
    } catch (error) {
        console.error("Error fetching Firebase config: ", error);
    }
});

document.getElementById('signin-form').addEventListener('input', function(event) {
    const userIdentifier = document.getElementById('usernamelog').value.trim();
    const password = document.getElementById('passwordlog').value.trim();
    const emaillog = document.getElementById('emaillog').value.trim();
    const additionalFields = document.getElementById('additional-fields');

    // Check if all fields are filled
    if (userIdentifier && password && emaillog) {
        additionalFields.style.display = 'block';
    } else {
        additionalFields.style.display = 'none';
    }
});

async function encryptData(data) {
    try {
        const response = await fetch('/encrypt', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ data: data })
        });
        const result = await response.json();
        return result.encrypted_data;
    } catch (error) {
        console.error("Error during encryption: ", error);
    }
}
