# MongoDB

MongoDB stores data records as documents (specifically BSON documents) which are gathered together in collections. A database stores one or more collections of documents.

MongoDB stores data records as BSON documents. BSON is a binary representation of JSON documents, though it contains more data types than JSON.

A MongoDB document.
{
Firstname : 'Laxman',        <-----------    Field : value
Lastname : 'Kumar',          <-----------    Field : value
Age : 25,                    <-----------    Field : value
Salary : 25000               <-----------    Field : value
}

Document Structure
MongoDB documents are composed of field-and-value pairs and have the following structure:

{
   field1: value1,
   field2: value2,
   field3: value3,
   ...
   fieldN: valueN
}

