PRAGMA foreign_keys = ON;

INSERT INTO category (categoryId, categoryName, categoryImage) VALUES
(1, 'Fiction', 'fiction.jpg'),
(2, 'Programming', 'programming.jpg'),
(3, 'Economics and Business', 'economics.jpg'),
(4, 'Science', 'science.jpg');

INSERT INTO book (bookId, categoryId, title, author, isbn, price, image, readNow) VALUES
(1, 1, '1984', 'George Orwell', '9780451524935', 12.99, '1984.jpg', 1),
(2, 1, 'Animal Farm', 'George Orwell', '9780451526342', 10.99, 'animal_farm.jpg', 1),
(3, 1, 'Pride and Prejudice', 'Jane Austen', '9780141439518', 11.99, 'pride.jpg', 0),
(4, 2, 'Python Crash Course', 'Eric Matthes', '9781718502703', 39.99, 'python_crash_course.jpg', 1),
(5, 2, 'Automate the Boring Stuff with Python', 'Al Sweigart', '9781593279929', 29.99, 'automate.jpg', 0),
(6, 2, 'Clean Code', 'Robert C. Martin', '9780132350884', 44.99, 'clean_code.jpg', 0),
(7, 3, 'Freakonomics', 'Steven D. Levitt and Stephen J. Dubner', '9780060731335', 16.99, 'freakonomics.jpg', 1),
(8, 3, 'Thinking, Fast and Slow', 'Daniel Kahneman', '9780374533557', 18.99, 'thinking.jpg', 0),
(9, 3, 'Capital in the Twenty-First Century', 'Thomas Piketty', '9780674430006', 35.00, 'capital.jpg', 0),
(10, 4, 'A Brief History of Time', 'Stephen Hawking', '9780553380163', 17.99, 'history_of_time.jpg', 1),
(11, 4, 'Cosmos', 'Carl Sagan', '9780345539434', 18.99, 'cosmos.jpg', 0),
(12, 4, 'The Selfish Gene', 'Richard Dawkins', '9780198788607', 19.99, 'selfish_gene.jpg', 0);
