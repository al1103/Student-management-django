    var myLocalStorageValue = localStorage.getItem('theme');
    if (myLocalStorageValue === null) {
        myLocalStorageValue = 'dark';
        localStorage.setItem('theme', myLocalStorageValue);
    }
    

    document.body.setAttribute('data-bs-theme', myLocalStorageValue);