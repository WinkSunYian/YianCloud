from db.models import UserMetadata


class UserMetadataRepository:
    @staticmethod
    async def get_by_user_id(user_id):
        """根据用户ID获取用户元数据"""
        return await UserMetadata.get(user_id=user_id)

    @staticmethod
    async def delete_by_user_id(user_id):
        """根据用户ID删除用户元数据"""
        await UserMetadata.delete().where(UserMetadata.user_id == user_id).execute()
