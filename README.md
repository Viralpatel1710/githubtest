# Student Registration Form - Issues in Original Code

This README documents the issues identified in the original HTML, CSS, and JavaScript code for the Student Registration Form. These issues were addressed in the refactored version of the code to improve functionality, accessibility, and maintainability.

## HTML Issues

1. **Nested `<form>` Tags**:
   - The code contains two nested `<form>` tags, which is invalid HTML. Nested forms are not supported and can lead to unpredictable behavior in browsers.
   - **Example**: An outer `<form>` tag wraps the inner `<form id="Registrationform">`.

2. **Incorrect `onsubmit` Attribute**:
   - The `onsubmit` attribute is written as `on submit` (with a space) and references `validateform()` (lowercase `f`), but the function is named `validateForm`. This prevents the validation function from being called.
   - **Example**: `<form id="Registrationform" on submit="return validateform()">`.

3. **HTML Syntax Errors in Radio Buttons**:
   - The `male` radio button input tag is incomplete, missing a closing `>`.
   - The `<label>` for `female` is empty, and the `Male` label is missing a closing `</label>` tag.
   - **Example**: 
     ```html
     <input type="radio" id="male" name="gender" value="male"
     <label for="male">Male
     <input type="radio" id="female" name="gender" value="Female" >Female
     <label for="female"> </label>
     ```

4. **Invalid Error `<div>` IDs**:
   - Error `<div>` IDs like `firstName error` and `LastName error` contain spaces, which are invalid in HTML. Other IDs like `emailerror` and `phoneerror` lack consistent naming conventions.
   - **Example**: `<div id="firstName error" class="error"></div>`.

## CSS Issues

1. **Excessive Form Width**:
   - The form has a `width: 1120%`, which is excessively large and causes layout issues, making the form unusable on most screens.
   - **Example**: `form { width: 1120%; }`.

2. **Invalid CSS Properties**:
   - The `border: radius 2cm` property in the `button` style is invalid; it should be `border-radius: 2cm`.
   - The `cursor: 75px` property is invalid; it should be `cursor: pointer`.
   - The `margin-bottom: px` in the `label` style is invalid due to a missing value.
   - **Example**: 
     ```css
     button {
         border: radius 2cm;
         cursor: 75px;
     }
     label {
         margin-bottom: px;
     }
     ```

3. **Unnecessary `display: -webkit-box`**:
   - The `label` style uses `display: -webkit-box`, which is unnecessary and may not achieve the intended layout effect.
   - **Example**: `label { display: -webkit-box; }`.

4. **Inconsistent Button Styling**:
   - The CSS targets `button` but does not style `<input type="submit">`, which could be used interchangeably, leading to inconsistent appearance.
   - **Example**: The submit button is a `<button>`, but no styles are applied to `<input type="submit">`.

## JavaScript Issues

1. **Case Mismatch in Form ID**:
   - The JavaScript references the form as `document.forms["registrationForm"]` (lowercase `r`), but the form's `id` is `Registrationform` (uppercase `R`). This causes a reference error.
   - **Example**: `let firstName = document.forms["registrationForm"]["firstName"].value.trim();`.

2. **Incorrect Password Regex**:
   - The password regex `^(?=.[a-z])(?=.[A-Z])(?=.\d)(?=.[@$!%?&])[A-Za-z\d@$!%?&]{8,}$` is invalid due to missing asterisks (`*`) in the lookaheads, causing it to fail.
   - **Example**: `let passwordPattern = /^(?=.[a-z])(?=.[A-Z])(?=.\d)(?=.[@$!%?&])[A-Za-z\d@$!%?&]{8,}$/;`.

3. **Improper Gender Validation**:
   - The gender validation checks `gender === ""`, but `document.forms["Registrationform"]["gender"].value` returns `undefined` when no radio button is selected, leading to incorrect validation.
   - **Example**: 
     ```javascript
     let gender = document.forms["registrationForm"]["gender"].value;
     if (gender === "") {
         alert("Please select your gender");
         return false;
     }
     ```

4. **Use of `alert` for Errors**:
   - Validation errors are displayed using `alert`, which provides a poor user experience and does not utilize the error `<div>` elements defined in the HTML.
   - **Example**: `alert("First name must contain only letters");`.

5. **Missing `event.preventDefault()`**:
   - The `validateForm` function does not call `event.preventDefault()`, which could allow the form to submit even if validation fails.
   - **Example**: The function lacks `event.preventDefault()` at the start.

## Accessibility Issues

1. **Lack of Accessibility Attributes**:
   - The form lacks `aria-*` attributes to link inputs with error messages, making it less accessible for screen reader users.
   - **Example**: No `aria-describedby` attributes on inputs to associate with error `<div>` elements.

2. **Poor Label Association**:
   - The gender radio buttons have incomplete or empty labels, which can confuse screen readers and users.
   - **Example**: `<label for="female"> </label>` is empty.

## Usability Issues

1. **Non-Responsive Design**:
   - The form's `width: 1120%` and fixed `height: 60vh` make it non-responsive, causing layout issues on smaller screens.
   - **Example**: `form { width: 1120%; height: 60vh; }`.

2. **Inconsistent Error Feedback**:
   - Error messages are not displayed in the designated `<div>` elements, and the use of `alert` interrupts the user experience.
   - **Example**: Error `<div>` elements like `<div id="firstNameError" class="error"></div>` are unused.

## Refactoring Notes

The refactored code addresses these issues by:
- Removing nested `<form>` tags and correcting HTML syntax.
- Fixing CSS properties and making the form responsive.
- Correcting JavaScript validation, including the password regex and gender validation.
- Displaying errors in `<div>` elements instead of `alert`.
- Adding accessibility attributes like `aria-describedby`.
- Ensuring consistent naming and styling.
- Adding `event.preventDefault()` to control form submission.

For the refactored code, see the main project files in the repository.