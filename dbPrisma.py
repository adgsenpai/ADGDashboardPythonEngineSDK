import asyncio
from prisma import Prisma

async def main():
    # Instantiate the Prisma client
    prisma = Prisma()

    # Connect to the database
    await prisma.connect()
    print("Connected to the database.")

    # ------------------------------
    # Create a new User record
    # ------------------------------
    new_user = await prisma.user.create(
        data={
            "name": "John",
            "surname": "Doe",
            "email": "john.doe@example.com",
            "country": "USA",
            "mobile": "1234567890",
            "password": "securepassword123"
        }
    )
    print("Created user:", new_user)

    # ------------------------------
    # Query all User records
    # ------------------------------
    users = await prisma.user.find_many()
    print("All users:", users)

    # ------------------------------
    # Update the created User's country
    # ------------------------------
    updated_user = await prisma.user.update(
        where={"id": new_user.id},
        data={"country": "Canada"}
    )
    print("Updated user:", updated_user)

    # ------------------------------
    # Delete the User record
    # ------------------------------
    deleted_user = await prisma.user.delete(
        where={"id": new_user.id}
    )
    print("Deleted user:", deleted_user)

    # Disconnect from the database
    await prisma.disconnect()
    print("Disconnected from the database.")

if __name__ == '__main__':
    asyncio.run(main())
