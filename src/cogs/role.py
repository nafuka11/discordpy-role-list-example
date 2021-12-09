import io
from logging import getLogger
from typing import List

from discord import File, Role
from discord.ext import commands

log = getLogger(__name__)


class RoleCog(commands.Cog):
    @commands.command(name="rolecsv")
    async def dump_role_csv(self, ctx: commands.Context):
        """Guildのrole一覧(id=roleの順序,permission)をcsvファイルで送信する"""
        roles: List[Role] = ctx.guild.roles
        csv_str = self.generate_csv_str(roles)
        data = io.BytesIO(csv_str.encode("utf-8"))
        await ctx.send(file=File(data, "role.csv"))

    def generate_csv_str(self, roles: List[Role]) -> str:
        """csvファイルの文字列を返す"""
        csv_header = f"id,name,{','.join([perm[0] for perm in roles[0].permissions])}"
        csv_rows = [csv_header]
        for role in roles:
            csv_row = f"{role.position},{role.name},{','.join([str(perm[1]) for perm in role.permissions])}"
            csv_rows.append(csv_row)
        csv_str = "\n".join(csv_rows)
        return csv_str
