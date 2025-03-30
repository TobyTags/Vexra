import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js";
import { getAuth, signInWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-auth.js";
import { getFirestore, collection, getDocs, addDoc, query, where, doc, setDoc, getDoc, runTransaction } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js";

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


        // This is for log in
        const loginForm = document.getElementById('login-form');
        if (loginForm) {
            loginForm.addEventListener('submit', async function(event) {
                event.preventDefault(); // Prevent form submission

                const userIdentifier = document.getElementById('user-identifier').value.trim();
                const password = document.getElementById('password').value.trim();

                // Validate that userIdentifier and password are provided
                if (!userIdentifier || !password) {
                    document.getElementById('user-identifier-error').textContent = 'Please enter your username or email address.';
                    document.getElementById('password-error').textContent = 'Please enter your password.';
                    return; // Stop execution if validation fails
                }

                // Clear previous error messages
                document.getElementById('user-identifier-error').textContent = '';
                document.getElementById('password-error').textContent = '';

                const userIdentifierenc = await encryptData(userIdentifier);
                const passwordenc = await encryptData(password);

                // Query to find user by username
                const usernameQuery = query(
                    collection(db, "WMLogin"),
                    where("username", "==", userIdentifierenc)
                );

                // Query to find user by email
                const emailQuery = query(
                    collection(db, "WMLogin"),
                    where("email", "==", userIdentifierenc)
                );

                // Perform both queries and handle results
                Promise.all([getDocs(usernameQuery), getDocs(emailQuery)])
                    .then(([usernameSnapshot, emailSnapshot]) => {
                        let userDoc = null;

                        // Check if any query returns a result
                        if (!usernameSnapshot.empty) {
                            userDoc = usernameSnapshot.docs[0].data();
                        } else if (!emailSnapshot.empty) {
                            userDoc = emailSnapshot.docs[0].data();
                        }

                        if (userDoc) {
                            if (userDoc.password === passwordenc) {
                                // Save the identifier (username or email) to local storage
                                localStorage.setItem('WMcreds', userDoc.username || userDoc.email);
                                localStorage.setItem('isAuthenticated', 'true');


                                window.location.href = '/logedin'; // Redirect to dashboard page
                            } else {
                                alert('Incorrect password!');
                            }
                        } else {
                            alert('User not found!');
                        }
                    })
                    .catch((error) => {
                        console.error("Error fetching documents: ", error);
                    });
            });
        }

    } catch (error) {
        console.error("Error fetching Firebase config: ", error);
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